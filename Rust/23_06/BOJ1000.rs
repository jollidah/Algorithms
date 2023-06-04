// A + B

use std::io;

fn main() {
    let mut a = String::new();
    io::stdin().read_line(&mut a).expect("shiver");
    let b: Vec<usize> = a.split_whitespace()
        .map(|s| s.trim().parse().expect("error"))
        .collect::<Vec<_>>();

    println!("{}", b[0] + b[1]);
}

https://www.acmicpc.net/problem/1000
