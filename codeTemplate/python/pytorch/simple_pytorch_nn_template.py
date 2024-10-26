import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from tqdm import tqdm

# 1. 设置超参数
batch_size = 64
learning_rate = 0.001
num_epochs = 5
save_model_path = "./simple_net.pth"

# 自动选择设备：GPU (cuda) 或 CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 2. 数据集准备（以 MNIST 数据集为例）
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

train_dataset = datasets.MNIST(root="./data", train=True, transform=transform, download=True)
test_dataset = datasets.MNIST(root="./data", train=False, transform=transform, download=True)

train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)


print(train_dataset[0])


# 3. 搭建神经网络模型
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128)  # 输入层：28x28 图像尺寸
        self.fc2 = nn.Linear(128, 64)  # 隐藏层
        self.fc3 = nn.Linear(64, 10)  # 输出层：10 个类别

    def forward(self, x):
        x = x.view(-1, 28 * 28)  # 将图像展平为向量
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)  # 不加激活函数，交给 CrossEntropyLoss 处理
        return x


model = SimpleNet().to(device)  # 模型加载到指定设备上

# 4. 设置损失函数和优化器
criterion = nn.CrossEntropyLoss()  # 适用于多分类任务
optimizer = optim.Adam(model.parameters(), lr=learning_rate)


# 5. 训练模型
def train_model():
    model.train()  # 设置模型为训练模式
    for epoch in range(num_epochs):
        correct = 0
        total = 0
        running_loss = 0.0
        progress_bar = tqdm(enumerate(train_loader), total=len(train_loader), desc=f"Epoch {epoch+1}/{num_epochs}")

        for i, (images, labels) in progress_bar:
            images, labels = images.to(device), labels.to(device)

            # 前向传播
            outputs = model(images)
            loss = criterion(outputs, labels)

            # 反向传播和优化
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total += labels.size(0)
            _, predicted = torch.max(outputs.data, 1)
            correct += (predicted == labels).sum().item()

            running_loss += loss.item()
            progress_bar.set_postfix(loss=loss.item(), accuracy=100 * correct / total)

        # 每个epoch结束时打印平均损失
        print(f"Epoch [{epoch+1}/{num_epochs}], Average Loss: {running_loss / len(train_loader):.4f}, Accuracy: {100 * correct / total:.2f}%")

    # 保存模型
    torch.save(model.state_dict(), save_model_path)
    print(f"Model saved to {save_model_path}")


# 6. 测试模型
def test_model():
    model.eval()  # 设置模型为评估模式
    correct = 0
    total = 0
    running_loss = 0.0
    with torch.no_grad():  # 评估时不需要计算梯度
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)
            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f"Test Loss: {running_loss / len(test_loader):.4f}, Test Accuracy: {100 * correct / total:.2f}%")


# 7. 加载模型
def load_model():
    try:
        model.load_state_dict(torch.load(save_model_path))
        model.to(device)
        print(f"Model loaded from {save_model_path}")
    except FileNotFoundError:
        print(f"No model found at {save_model_path}, starting training from scratch")


# 8. 执行训练、测试和加载模型
load_model()  # 可选：如果存在之前训练的模型，则加载模型
train_model()
test_model()
