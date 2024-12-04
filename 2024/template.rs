use std::fs::File;
use std::io::{BufRead, BufReader, Error};

#[derive(Default, Clone, Debug)]
struct Puzzle {
    prop: i32,
}

fn parse_puzzle() -> Result<Puzzle, Error> {
    let file = File::open("./input.txt")?;
    let reader = BufReader::new(file);

    let mut puzzle: Puzzle = Puzzle::default();

    for line in reader.lines() {
        // do something
    }

    Ok(puzzle)
}

fn solve_part_one(puzzle: &Puzzle) -> Result<i32, Error> {
    Ok(0)
}

/*
*************************
        part 2
*************************
*/

fn solve_part_two(puzzle: &Puzzle) -> Result<i32, Error> {
    Ok(0)
}

fn main() -> () {
    let puzzle = parse_puzzle().unwrap();

    let res1 = solve_part_one(&puzzle).unwrap();
    println!("result1: {}", res1);

    let res2 = solve_part_two(&puzzle).unwrap();
    println!("result2: {}", res2);
}
