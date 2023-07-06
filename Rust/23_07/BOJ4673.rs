// 셀프 넘버

use std::io::{BufWriter, Write, stdout};

fn check(mut n : i32) -> usize{
    let mut tmp : i32 = n;
    while n != 0{
        tmp += n % 10;
        n /= 10;
    }
    tmp as usize
}

fn main() {
    let mut writer = BufWriter::new(stdout().lock());
    let mut non_self : [bool; 10000] = [true; 10000];
    for num in 1..10000 {
        let idx : usize = check(num);
        if idx < 10000{
            non_self[idx] = false;
        }
        if non_self[num as usize]{
            writeln!(writer, "{}", num).unwrap();
        }
    }
}

// https://www.acmicpc.net/problem/4673
