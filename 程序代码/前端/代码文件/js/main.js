document.addEventListener('DOMContentLoaded', function () {
    const inputArea = document.getElementById('input-area');
    const submitDataButton = document.getElementById('submit-data');

    inputArea.addEventListener('paste', function (event) {
        const items = (event.clipboardData || window.clipboardData).items;

        for (const item of items) {
            if (item.type.indexOf('image') !== -1) {
                const file = item.getAsFile();
                const reader = new FileReader();

                reader.onload = function (event) {
                    const img = document.createElement('img');
                    img.src = event.target.result;
                    inputArea.appendChild(img);
                };

                reader.readAsDataURL(file);
                event.preventDefault();
            }
        }
    });


    submitDataButton.addEventListener('click', async function () {
        const inputAreaContent = inputArea.innerHTML;

        try {
            const response = await fetch('/upload', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ content: inputAreaContent }),
            });

            if (response.ok) {
                console.log('数据发送成功');
            } else {
                console.error('数据发送失败:', response.statusText);
            }
        } catch (error) {
            console.error('数据发送失败:', error);
        }
    });
});

