// 크로아티아 알파벳

use std::{io::stdin, collections::HashSet, process::exit};

fn main(){
    let mut threed_long_set: HashSet<String> = HashSet::new();
    threed_long_set.insert(String::from("dz="));
    let mut two_long_set: HashSet<String> = HashSet::new();
    two_long_set.insert(String::from("lj"));
    two_long_set.insert(String::from("nj"));
    two_long_set.insert(String::from("c="));
    two_long_set.insert(String::from("c-"));
    two_long_set.insert(String::from("d-"));
    two_long_set.insert(String::from("s="));
    two_long_set.insert(String::from("z="));
    let mut buffer = String::new();
    stdin().read_line( &mut buffer).unwrap();
    let buffer = buffer.trim();
    if buffer.len() == 1{
        println!("1");
        exit(0);
    }
    let mut idx = 0;
    let mut res = 0;
    loop {
        if idx < buffer.len() - 2 && threed_long_set.contains(&buffer[idx..idx + 3]){

            idx += 3;
        }else if idx < buffer.len() - 1 && two_long_set.contains(&buffer[idx..idx + 2]){
            idx += 2;

        } else if idx != buffer.len(){
            idx += 1;
        } else{
            break;
        }
        res += 1;
    }
    println!("{}", res);
}

// https://www.acmicpc.net/problem/2941