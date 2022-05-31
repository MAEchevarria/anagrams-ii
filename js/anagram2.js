exports.anagramsFor = function(word, listOfWords) {
// # Anagram Part II - This time you're going to check a word against a list of other words.
// ## Premise - The goal of this exercise is to return a new list of all the anagrams from the provided list.
// ## Example - anagrams_for("saltier", ["cognac", "saltier", "realist", "retails"]) == ["saltier", "realist", "retails"]
// ## Challenge Yourself - * Try to break your method up so that they only have a single job to do.
    
    // return an array of string matches or empty array
    let outputArr = []; 
    let wordsArr = listOfWords;    
    let comparisonWord = word.split("").sort().join("");

    for (let i = 0; i < wordsArr.length; i++){
        let sortedStr = wordsArr[i].split("").sort().join("");
        if (sortedStr === comparisonWord) {
            outputArr.push(wordsArr[i]);
        }
    }

    return outputArr;

};
