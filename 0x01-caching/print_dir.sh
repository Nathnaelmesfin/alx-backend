#!/bin/bash

echo "Current directory: $(pwd)"
echo

function print_tree {
    local dir="$1"
    local prefix="$2"
    local num_children=$(ls -1 "$dir" | wc -l)
    local count=1

    for child in "$dir"/*; do
        local child_name="$(basename "$child")"
        if [ -d "$child" ]; then
            printf "${prefix}├── %s/\n" "$child_name"
            print_tree "$child" "$prefix│   "
        else
            printf "${prefix}├── %s\n" "$child_name"
        fi

        if [ "$count" -eq "$num_children" ]; then
            prefix="${prefix::-4}"
            printf "${prefix}└──\n"
        fi

        count=$((count+1))
    done
}

print_tree "$(pwd)" ""

