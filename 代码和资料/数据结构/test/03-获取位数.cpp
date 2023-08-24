#include <iostream>
#include <bitset>
#include <math.h>
#include <iomanip>
template<typename T>
struct FloatRepresentation {};

template<>
struct FloatRepresentation<float> {
    uint32_t bits;
    static const int signBits = 1;
    static const int exponentBits = 8;
    static const int mantissaBits = 23;
};

template<>
struct FloatRepresentation<double> {
    uint64_t bits;
    static const int signBits = 1;
    static const int exponentBits = 11;
    static const int mantissaBits = 52;
};

template <typename T>
void printFloatComponents(T value) {
    FloatRepresentation<T> rep;
    rep.bits = *reinterpret_cast<decltype(rep.bits)*>(&value);

    auto sign_mask = (decltype(rep.bits))(1) << (FloatRepresentation<T>::exponentBits + FloatRepresentation<T>::mantissaBits);
    auto exponent_mask = ((decltype(rep.bits))(1) << FloatRepresentation<T>::exponentBits) - 1;
    exponent_mask <<= FloatRepresentation<T>::mantissaBits;
    auto mantissa_mask = ((decltype(rep.bits))(1) << FloatRepresentation<T>::mantissaBits) - 1;

    auto sign = (rep.bits & sign_mask) >> (FloatRepresentation<T>::exponentBits + FloatRepresentation<T>::mantissaBits);
    auto exponent = (rep.bits & exponent_mask) >> FloatRepresentation<T>::mantissaBits;
    auto mantissa = rep.bits & mantissa_mask;

    std::cout << "Value: " << value << "\n";
    std::cout << "Sign: " << std::bitset<FloatRepresentation<T>::signBits>(sign) << "\n";
    std::cout << "Exponent: " << std::bitset<FloatRepresentation<T>::exponentBits>(exponent) << "\n";
    std::cout << "Mantissa: " << std::bitset<FloatRepresentation<T>::mantissaBits>(mantissa) << "\n";
    std::cout << "-----------------------------" << std::endl;
}

int main() {
    float f_val = 0.3;
    double d_val = -0.15625;

    printFloatComponents(f_val);
    //printFloatComponents(d_val);

    std::cout << f_val << std::endl;
    std::cout << std::setprecision(10) << f_val << std::endl;

    std::cout << pow(f_val, 1000) << std::endl;

    std::cout << 0.0 / 0 << std::endl;

    return 0;
}
