use std::fs::File;
use std::io::{BufReader, BufRead, Error};
use std::collections::HashMap;


#[derive(Default, Clone, Debug)]
struct Puzzle {
    column1: Vec<i32>,
    column2: Vec<i32>,
}

fn parse_puzzle() -> Result<Puzzle, Error> {
    let file = File::open("./input.txt")?;
    let reader = BufReader::new(file);

    let mut res:Puzzle = Puzzle::default();

    for line in reader.lines() {
        let parts:Vec<i32> = line?
            .trim()
            .split("   ")
            .map(|s| s.parse().unwrap_or(0))
            .collect();

        res.column1.push(parts[0]);
        res.column2.push(parts[1]);
    }

    Ok(res)
}


fn solve_part_one(puzzle:&Puzzle)-> Result<i32, Error>{
    let mut tmp:Puzzle = puzzle.clone();

    tmp.column1.sort();
    tmp.column2.sort();

    let mut tot:i32 = 0;
    for (i, _) in tmp.column1.iter().enumerate() {
        tot += (tmp.column1[i] - tmp.column2[i]).abs();
    }

    Ok(tot)
}

/*
*************************
        part 2
*************************
*/

fn sum_of_products(map:&HashMap<i32, i32>) -> i32 {
    let mut tot = 0;
    for key in map.keys(){
        let value = map.get(key).unwrap_or(&0);
        tot += *key * value;
    }

    tot
}

fn solve_part_two(puzzle:&Puzzle)-> Result<i32, Error>{
    let mut d = HashMap::new();

    for x in puzzle.column1.iter() {
        d.insert(*x, 0);
    }

    for x in puzzle.column2.iter(){
        if d.contains_key(x) {
            *d.entry(*x).or_insert(0) += 1;
        }
    }

    let result = sum_of_products(&d);
    Ok(result)
}


fn main() -> () {
    let puzzle = parse_puzzle().unwrap();

    let res1 = solve_part_one(&puzzle).unwrap();
    println!("result1: {}", res1);

    let res2 = solve_part_two(&puzzle).unwrap();
    println!("result2: {}", res2);
}
