#!/bin/bash

#Variable declarations
DIR="$( cd "$( dirname "${BASH_SOURCE[1]}" )" && pwd )"
NGINX_LOG_FILE_LOC="$DIR/../logs/nginx-access.log"

testArray=("blue" "green" "red" "green")

declare -a awkTestArray

mapfile -t awkTestArray < "$NGINX_LOG_FILE_LOC"


function testAssociatedArray() {
    for element in "${testArray[@]}";do
        echo $element
    done

    declare -A countArray

    for element in "${testArray[@]}";do
        ((countArray["$element"]++))
    done

    echo ${!countArray[@]}
    echo ${countArray[@]}

}

function testAWK(){

    for key in "${awkTestArray[@]}"; do
        echo "$key"
    done

}

testAWK
