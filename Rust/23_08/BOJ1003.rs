// 피보나치 함수
// "s3 / 35m"
use std::{io::stdin, cmp::max};

fn main(){
    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();
    let n = input.trim().parse::<i32>().unwrap();
    let mut dp:Vec<[i32; 2]> = vec![[1, 0], [0, 1]];
    let mut idx = 2;
    for _ in 0..n{
        input.clear();
        stdin().read_line(& mut input).unwrap();
        let num = input.trim().parse::<i32>().unwrap();
        for i in idx..(num + 1) as usize{
            dp.push([dp[i - 2][0] + dp[i - 1][0],
                     dp[i - 2][1] + dp[i - 1][1]]);
        }
        idx = max(idx, (num + 1) as usize);
        println!("{} {}", dp[num as usize][0], dp[num as usize][1]);
    }
}

// https://www.acmicpc.net/problem/1003