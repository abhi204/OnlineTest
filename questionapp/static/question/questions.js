function editQ(q_id){
    var listItem = document.querySelector(`#${q_id}`);
    var {answer, question, qtype} = listItem.dataset
    document.querySelector('#editAns').value = answer
    document.querySelector('#editQuestion').value = question
    document.querySelector('#edit_qid').value = q_id;
    document.querySelector("#edit_qtype").value = qtype;
    if(listItem.dataset.qtype == 'mcq')
    {
      document.querySelector("#editOptions").style.display = 'inherit';
      var {opta, optb, optc, optd} = listItem.dataset;
      document.querySelector("#editOptA").value = opta;
      document.querySelector("#editOptB").value = optb;
      document.querySelector("#editOptC").value = optc;
      document.querySelector("#editOptD").value = optd;
    }
    else{
      document.querySelector("#editOptions").style.display = 'none';
    }
  };