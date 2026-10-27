#!/usr/bin/env python3
"""Calcula contraste WCAG entre dos colores HEX."""
import re, sys

def rgb(hex_color: str):
    value = hex_color.strip().lstrip('#')
    if len(value) == 3:
        value = ''.join(c * 2 for c in value)
    if not re.fullmatch(r'[0-9a-fA-F]{6}', value):
        raise ValueError(f'Color HEX inválido: {hex_color}')
    return tuple(int(value[i:i+2], 16) / 255 for i in (0,2,4))

def linear(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def luminance(hex_color: str) -> float:
    r,g,b = (linear(c) for c in rgb(hex_color))
    return 0.2126*r + 0.7152*g + 0.0722*b

def contrast(a: str, b: str) -> float:
    l1,l2 = sorted((luminance(a), luminance(b)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)

def main():
    if len(sys.argv) != 3:
        print('Uso: check_contrast.py <#foreground> <#background>')
        return 2
    try:
        ratio = contrast(sys.argv[1], sys.argv[2])
    except ValueError as exc:
        print(f'ERROR: {exc}')
        return 2
    print(f'Contraste: {ratio:.2f}:1')
    print('Texto normal (4.5:1):', 'PASS' if ratio >= 4.5 else 'FAIL')
    print('Texto grande (3:1):', 'PASS' if ratio >= 3 else 'FAIL')
    print('Componentes/UI (3:1):', 'PASS' if ratio >= 3 else 'FAIL')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
