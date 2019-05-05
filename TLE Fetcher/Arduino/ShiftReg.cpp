#include "ShiftReg.h"

ShiftReg::ShiftReg()
{
    SHIFT_SIZE = 4;
    buf = new uint8_t[SHIFT_SIZE];
}

ShiftReg::ShiftReg(uint8_t size)
{
    SHIFT_SIZE = size;
    buf = new uint8_t[SHIFT_SIZE];
}

ShiftReg::~ShiftReg()
{
    delete [] buf;
}

void ShiftReg::input(uint8_t byte)
{
    for(int i = 0; i < SHIFT_SIZE - 1; i++)
    {
        buf[i] = buf[i + 1];
    }

    buf[SHIFT_SIZE] = byte;
}

int ShiftReg::get(int index)
{
    if(index < 0 || index >= SHIFT_SIZE)
        return -1;

    return buf[index];
}

bool ShiftReg::validate(uint8_t* in_buf)
{
    for(int i = 0; i < SHIFT_SIZE; i++)
    {
        if(in_buf[i] != buf[i])
            return false;
    }

    return true;
}

bool ShiftReg::validate(uint8_t* in_buf, bool reverse)
{
    if(reverse)
    {
        uint8_t tmp_buf[SHIFT_SIZE];
        for(int i = 0; i < SHIFT_SIZE; i++)
        {
            tmp_buf[SHIFT_SIZE - i - 1] = in_buf[i];
        }

        return validate(tmp_buf);
    }

    return validate(in_buf);
}

void ShiftReg::flush()
{
    for(int i = 0; i < SHIFT_SIZE; i++)
    {
        buf[i] = 0x00;
    }
}