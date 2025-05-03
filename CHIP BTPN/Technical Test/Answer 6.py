function calculateSaving(n) {
    let totalMoney = 0;
    let addMonday = 1;
    while (n > 0) {
        for (let day = 0; day < Math.min(n, 7); day++) {
            totalMoney += addMonday + day;
        }
        n -= 7;
        addMonday++;
    }
    return totalMoney;
}
