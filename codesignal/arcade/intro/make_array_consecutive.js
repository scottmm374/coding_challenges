// Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

// Example

// For statues = [6, 2, 3, 8], the output should be
// solution(statues) = 3.

// Ratiorg needs statues of sizes 4, 5 and 7.

// Input/Output

//     [execution time limit] 4 seconds (js)

//     [input] array.integer statues

//     An array of distinct non-negative integers.

//     Guaranteed constraints:
//     1 ≤ statues.length ≤ 10,
//     0 ≤ statues[i] ≤ 20.

//     [output] integer

//     The minimal number of statues that need to be added to existing statues such that it contains every integer size from an interval [L, R] (for some L, R) and no other sizes.

// https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC/solutions?solutionId=hZPuPHANGowkgTBYP

function solution(statues) {
  let sortStatueArr = statues.sort((a, b) => a - b);
  let count = 0;
  let i = 0;
  if (statues.length <= 1) {
    return 0;
  } else {
    while (i < sortStatueArr.length - 1) {
      let diff = sortStatueArr[i + 1] - sortStatueArr[i];
      if (diff === 1) {
        i += 1;
      } else {
        count = count + (diff - 1);
        i += 1;
      }
    }
  }
  return count;
}
