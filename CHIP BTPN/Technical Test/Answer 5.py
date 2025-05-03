function findMinimumDifference(packets, participants) {
    packets.sort((a, b) => a - b);
 
    let diffPackets = Infinity;
    let selectedPackets = [];
    let myArray = [];
 
    for (let i = 0; i <= packets.length - participants; i++) {
        let difference = packets[i + participants - 1] - packets[i];
 
        if (difference < diffPackets) {
            diffPackets = difference;
            selectedPackets = packets.slice(i, i + participants);
        }
    }
    
    myArray.push(selectedPackets);
    
    let formattedString = diffPackets + ', [' + myArray + ']';
    return [formattedString];
}
