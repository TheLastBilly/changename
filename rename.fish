#!/usr/bin/fish
function rename_loop
    for f in $argv
        if test -d $f
            rename_loop $f/*
        else
            changename -i -t name1 -r name2 -f $f
        end
    end
end

rename_loop ./*
