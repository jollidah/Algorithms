// 랜선 자르기

use std::io::stdin;

fn main(){
    let mut buffer = String::new();
    stdin().read_line( &mut buffer).unwrap();
    let mut it = buffer.split_whitespace();
    let k: i64 = it.next().unwrap().parse().unwrap();
    let n: i64 = it.next().unwrap().parse().unwrap();
    buffer.clear();
    let mut n_list: Vec<i64> = Vec::new();
    let mut max_v: i64 = 0;
    for _ in 0..k{
        stdin().read_line(& mut buffer).unwrap();
        let num = buffer.trim().parse::<i64>().unwrap();
        max_v = max_v.max(num);
        n_list.push(num);
        buffer.clear();
    }
    let mut cnt;
    let mut lp = 1;
    let mut rp = max_v;
    while lp <= rp{
        cnt = 0;
        let mid = (lp + rp) / 2;
        for num in &n_list{
            cnt += *num / mid;
        }
        if cnt >= n {
            lp = mid + 1;
        } else {
            rp = mid - 1;
        }
    }
    println!("{}", rp);
}

// https://www.acmicpc.net/problem/1654