// 소수 구하기

use std::{io::stdin, fmt::Write};

fn main() {
    let mut buffer = String::new();
    let mut writer = String::new();
    stdin().read_line(&mut buffer).unwrap();   
    let mut buffer = buffer.split_ascii_whitespace().flat_map(str::parse::<i32>);
    let a = buffer.next().unwrap();
    let b: i32 = buffer.next().unwrap();
    let mut n_list: Vec<i32> = (2..b + 1).collect();

    for n in 0..((b + 1) as f32).sqrt() as usize{ 
        if n_list[n] != 0{
            if n_list[n] >= a{
                writeln!(&mut writer, "{}",n_list[n]).unwrap();
            }
            for i in (n + 1)..n_list.len(){
                if n_list[i] % (n_list[n] as i32) == 0{
                    n_list[i] = 0;
                }
            }
        }
    }
    for n in (((b + 1) as f32).sqrt() as usize)..n_list.len(){ 
        if n_list[n] >= a{
            writeln!(&mut writer, "{}",n_list[n]).unwrap();
        }
    }
    println!("{}", writer);
}

// https://www.acmicpc.net/problem/1929