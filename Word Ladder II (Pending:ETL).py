#		hit	hot	dot	dog	lot	log	cog
#	hit	-1	1	0	0	0	0	0
#	hot	1	-1	1	0	1	0	0
#	dot	0	1	-1	1	1	0	0
#	dog	0	0	1	-1	0	1	1
#	lot	0	1	1	0	-1	1	0
#	log	0	0	0	1	1	-1	1
#	cog	0	0	0	1	0	1	-1

class Solution:
	# @param start, a string
	# @param end, a string
	# @param dict, a set of string
	# @return a list of lists of string

	def findLadders(self, start, end, dict):
		dlist = list(dict);
		dlist.append(start);
		dlist.append(end);
		adjMap = self.initMap(dlist);
		print(adjMap);
		return self.BFS(start, end, adjMap);
	
	def initMap(self, dict):
		def isNextTo(str_a, str_b):
			if len(str_a) != len(str_b):
				return False;
			
			diff = 0;
			for i in range(len(str_a)):
				if str_a[i] != str_b[i]:
					diff+=1;
			return (diff == 1);

		m={};
		for word_a in dict:
			m[word_a]=[];
			for word_b in dict:
				if isNextTo(word_a, word_b):
					m[word_a].append(word_b);
		return m;
	
	
	def BFS(self, start, end, dict):

		def find(searched, end, dict):
			searching = [];
			for path in searched:
				nx = dict.get(path[-1]);
				if(nx == []):
					result.append([]);
				#if end not in nx:
				for n in nx:
					if n not in path:
						tmp = path[:];
						tmp.append(n);
						if n == end:
							result.append(tmp);
							break;
						else:
							if(len(result) == 0):
								searching.append(tmp);
					
			return searching;

		result = [];
		searched = [[None]];
		searched[0][0] = start;
		while len(result) == 0:
			searched = find(searched, end, dict);
		return result;


	def DFS(self, start, end, dict):

		def find(start, end, dict, path):		
			for nx in dict.get(start):
				if nx not in path:
					tmp = path[:];
					tmp.append(nx);
					if nx == end:
						result.append(tmp);
						return;
					else:
						#if not (len(result) > 0 and len(path) < len(result[0])):
						find(nx, end, dict, tmp);

		result = [];
		path = [];
		path.append(start);
		find(start, end, dict, path);
		return result;
