#pragma once

#include <Arduino.h>

class ShiftReg
{
public:
    uint8_t SHIFT_SIZE;
private:
    uint8_t* buf;
public:
    ShiftReg();
    ShiftReg(uint8_t size);
    ~ShiftReg();

    void input(uint8_t byte);
    int get(int index);
    bool validate(uint8_t* in_buf);
    bool validate(uint8_t* in_buf, bool reverse);
    void flush();
    // perhaps add uint8_t* get() fnc later
};