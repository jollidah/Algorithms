fn main() {
    use std::{collections::VecDeque, io::stdin, process::exit};
    
    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();
    
    let byte_array = input.trim().as_bytes();
    let mut odd_cnt: u8 = 0;
    let mut res = VecDeque::with_capacity(byte_array.len());
    let mut char_array: [u8; 91] = [0; 91];
    for c in byte_array {
        char_array[*c as usize] += 1;
    }

    for i in (65..91).rev() {
        let cnt = char_array[i];
        let inserting_char = i as u8;

        if cnt % 2== 1{
            if odd_cnt == 1 {
                println!("I'm Sorry Hansoo");
                exit(0);
            }
            odd_cnt += 1;
            res.insert(res.len() / 2, inserting_char)
        }
        for _ in 0..(cnt / 2){
            res.push_back(inserting_char);
            res.push_front(inserting_char);
        }
    }

    println!("{:}", String::from_utf8(Vec::from(res)).unwrap())
}