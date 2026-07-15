#!/usr/bin/bash
rm -rf splits
mkdir -p splits
split -n l/4 -d entrada.txt splits/part_ --additional-suffix=.txt
echo "Archivo entrada.txt dividido en 4 partes dentro de splits/"
