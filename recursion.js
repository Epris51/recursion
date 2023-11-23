/** product: calculate the product of an array of numbers. */

function product(nums) {
  if (nums.length === 0) {
    return 1; // Return 1 for an empty array.
  }

  let result = 1;
  for (let num of nums) {
    result *= num;
  }
  return result;
}


/** longest: return the length of the longest word in an array of words. */

function longest(words) {
  let maxLength = 0;

  for (let word of words) {
    if (word.length > maxLength) {
      maxLength = word.length;
    }
  }

  return maxLength;
}

/** everyOther: return a string with every other letter. */

function everyOther(str) {
  let result = '';
  
  for (let i = 0; i < str.length; i += 2) {
    result += str[i];
  }
  
  return result;
}

/** isPalindrome: checks whether a string is a palindrome or not. */

function isPalindrome(str) {
  const cleanStr = str.toLowerCase().replace(/[^a-zA-Z0-9]/g, ''); // Remove non-alphanumeric characters and convert to lowercase.
  const reversedStr = cleanStr.split('').reverse().join('');
  return cleanStr === reversedStr;
}


/** findIndex: return the index of val in arr (or -1 if val is not present). */

function findIndex(arr, val) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === val) {
      return i;
    }
  }
  return -1;
}


/** revString: return a copy of a string, but in reverse. */

function revString(str) {
  return str.split('').reverse().join('');
}


/** gatherStrings: given an object, return an array of all of the string values. */

function gatherStrings(obj) {
  const strings = [];

  function gather(obj) {
    for (let key in obj) {
      if (typeof obj[key] === 'string') {
        strings.push(obj[key]);
      } else if (typeof obj[key] === 'object') {
        gather(obj[key]);
      }
    }
  }

  gather(obj);
  return strings;
}

/** binarySearch: given a sorted array of numbers, and a value,
 * return the index of that value (or -1 if val is not present). */

function binarySearch(arr, val) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] === val) {
      return mid;
    } else if (arr[mid] < val) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1; // Value not found.
}


module.exports = {
  product,
  longest,
  everyOther,
  isPalindrome,
  findIndex,
  revString,
  gatherStrings,
  binarySearch
};
