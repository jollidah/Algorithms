// 숨바꼭질

use std::{io::stdin, collections::VecDeque};

fn main(){
    let mut buffer = String::new();
    stdin().read_line( &mut buffer).unwrap();
    let mut iter = buffer.split_whitespace();
    let start = iter.next().unwrap().parse::<i32>().unwrap();
    let target = iter.next().unwrap().parse::<i32>().unwrap();
    let mut visit = vec![false ; (target * 2) as usize];
    let mut q: VecDeque<[i32; 2]> = VecDeque::new();
    let mut res = 1e9 as i32;
    q.push_back([start, 0]);
    while !q.is_empty(){
        let tmp = q.pop_front().unwrap();
        if tmp[0] == target {
            res = res.min(tmp[1]);
            break;
        } 
        if tmp[0] > target {
            res = res.min(tmp[0] - target + tmp[1]);
            continue;
        }
        if visit[tmp[0] as usize]{
            continue;
        }
        visit[tmp[0] as usize] = true;
        q.push_back([tmp[0] * 2, tmp[1] + 1]);
        q.push_back([tmp[0] + 1, tmp[1] + 1]);
        if tmp[0] != 0{
            q.push_back([tmp[0] - 1, tmp[1] + 1]);
        }
    }
    println!("{}", res);
}

// https://www.acmicpc.net/problem/1697