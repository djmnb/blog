#include <iostream>
#include <Windows.h>

int main() {
    DWORD targetPID = 14012;
    uintptr_t targetAddress = 0x403010;

    HANDLE hProcess = OpenProcess(PROCESS_VM_READ | PROCESS_VM_WRITE | PROCESS_VM_OPERATION, FALSE, targetPID);
    if (hProcess) {
        int newValue = 20;
        if (WriteProcessMemory(hProcess, (LPVOID)targetAddress, &newValue, sizeof(newValue), nullptr)) {
            std::cout << "Memory updated successfully!" << std::endl;
        } else {
            std::cout << "Failed to write to target memory." << std::endl;
        }

        CloseHandle(hProcess);
    } else {
        std::cout << "Failed to open target process." << std::endl;
    }

    return 0;
}
