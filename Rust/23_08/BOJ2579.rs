// 계단 오르기

use std::{ io::stdin, vec, cmp::max};

fn main() {
    let mut buffer = String::new();

    stdin().read_line(& mut buffer).unwrap();
    let n: i32 = buffer.trim().parse().unwrap();
    buffer.clear();
    for _ in 0..n{
        stdin().read_line(& mut buffer).unwrap();
    }
    let mut nList: Vec<i32> = buffer.split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect();
    nList.push(0);
    let mut dp = vec![[0; 2]; (n + 1) as usize];
    dp[0][0] = nList[0];
    if n != 1{
        dp[1][0] = nList[1];
    }
    for i in 0..(n - 1) as usize{
        dp[i + 1][1] = max(dp[i + 1][1], dp[i][0] + nList[i + 1]);
        dp[i + 2][0] = max(dp[i + 2][0], dp[i][0] + nList[i + 2]);
        dp[i + 2][0] = max(dp[i + 2][0], dp[i][1] + nList[i + 2]);
    }
    println!("{}", dp[(n - 1) as usize].iter().max().unwrap());
}

// https://www.acmicpc.net/problem/2579