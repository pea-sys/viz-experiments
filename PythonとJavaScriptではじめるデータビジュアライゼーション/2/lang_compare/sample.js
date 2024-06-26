let studentData = [
    { name: "Bob", id: 0, scores: [68, 75, 56, 81] },
    { name: "Alice", id: 1, scores: [75, 90, 64, 88] },
    { name: "Carol", id: 2, scores: [59, 74, 71, 68] },
    { name: "Dan", id: 3, scores: [64, 58, 53, 62] }
  ];
  
  function processStudentData(data, passThreshold = 60, meritThreshold = 75) {
    data.forEach(sdata => {
      let av = sdata.scores.reduce((prev, current) => prev + current, 0) / sdata.scores.length;
      sdata.average = av;
  
      if (av > meritThreshold) {
        sdata.assessment = 'passed with merit';
      } else if (av > passThreshold) {
        sdata.assessment = 'passed';
      } else {
        sdata.assessment = 'failed';
      }
  
      console.log(`${sdata.name}'s (id : ${sdata.id}) final assessment is : ${sdata.assessment.toUpperCase()}`);
    });
  }
  
  processStudentData(studentData);
  