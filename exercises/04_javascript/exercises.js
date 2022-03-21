function keywordusage(a, b) {
	for (i=0; i < b.length; i++){
		if (a.indexOf(b[i]) != -1){
			b[i]= true;
		}
		else{
			b[i]= false;
		}
	}
	return b;	
}

function frequencies(te, woli){
	var words = te.split(/\s/);
	var o = {};
	words.forEach(function(w){
	if (woli && woli.indexOf(w) > -1){
		if (!o[w]){
			o[w] = 0;
		}
		o[w] += 1;
	}
	});
	return o;
}

function rotate(array, steps){
	if (steps == 0){
		return array;
	}
	else if (steps < 0){
		for (i = 0; i>= steps % 4; i--){
			var first = array.shift();
			array.push(first);
		}
	}
	else{
		for (i = 0; i<= steps -1; i++){
			var last = array.pop();
			array.unshift(last);
		}
	}
	return array;
}

function rotate(array){
	var last = array.pop();
	array.unshift(last);
	return array;
}