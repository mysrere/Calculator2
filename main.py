#!/bin/bash

LOG="/home/calc_errors.log"

log_error() {
    echo "$(date): $1" >> "$LOG"
}

if [ $# -ne 3 ]; then
    echo "Использование: $0 {add|sub|mul|div} число1 число2"
    log_error "Неверное количество аргументов"
    exit 1
fi

operation="$1"
a="$2"
b="$3"

if ! [[ "$a" =~ ^-?[0-9]+([.][0-9]+)?$ ]] || ! [[ "$b" =~ ^-?[0-9]+([.][0-9]+)?$ ]]; then
    echo "Ошибка: аргументы должны быть числами"
    log_error "Переданы некорректные числа: $a $b"
    exit 1
fi

case "$operation" in
    add)
        awk "BEGIN {print $a + $b}"
        ;;
    sub)
        awk "BEGIN {print $a - $b}"
        ;;
    mul)
        awk "BEGIN {print $a * $b}"
        ;;
    div)
        if [ "$b" = "0" ] || [ "$b" = "0.0" ]; then
            echo "Ошибка: деление на ноль"
            log_error "Попытка деления на ноль"
            exit 1
        fi
        awk "BEGIN {print $a / $b}"
        ;;
    *)
        echo "Ошибка: неизвестная операция"
        log_error "Неизвестная операция: $operation"
        exit 1
        ;;
esac
