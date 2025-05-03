function miniGitWorks(lastCode, newCode) {
    let resultChange = "";
    let i = 0;
 
    while (i < lastCode.length && i < newCode.length) {
        if (lastCode[i] !== newCode[i]) {
            let j = i + 1;
            while (j < lastCode.length && j < newCode.length && lastCode[j] !== newCode[j]) {
                j++;
            }
            resultChange += `[${lastCode.substring(i, j)}|${newCode.substring(i, j)}]`;
            i = j;
        } else {
            resultChange += lastCode[i];
            i++;
        }
    }
 
    if (i < lastCode.length) {
        resultChange += `[${lastCode.substring(i)}]`;
    } else if (i < newCode.length) {
        resultChange += `[${newCode.substring(i)}]`;
    }
 
    return resultChange;
}
