// 괄호

use std::{io::stdin, fmt::Write, collections::VecDeque};

fn main() {
    let open : u8 = "(".as_bytes()[0];
	let mut buffer = String::new();
    let mut output = String::new();
    stdin().read_line(&mut buffer).unwrap();
    let n : i32 = buffer.trim().parse().unwrap();
    for _ in 0..n{
        let mut is_finish : bool = false;
        buffer.clear();
        stdin().read_line(&mut buffer).unwrap();
        let input = buffer.trim().as_bytes();
        let mut stack: VecDeque<bool> = VecDeque::new();
        // println!("{:#?}", input);
        for i in 0..buffer.trim().len(){
            if input[i] == open{
                stack.push_back(true);
            } else if !stack.is_empty() && stack.back() == Some(&true){
                stack.pop_back();
            } else {
                writeln!(output, "NO").unwrap();
                is_finish = true;
                break;
            }
        } 
        if !is_finish{
            if stack.is_empty() {
                writeln!(output, "YES").unwrap();
            } else {
                writeln!(output, "NO").unwrap();
            }
        }
    }
    println!("{output}");
}

// https://www.acmicpc.net/problem/9012
