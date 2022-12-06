import os
import random

#====================================
# Initialize params
d_from = 300
d_to = 10
commits_range = [1, 5]
#====================================

def file_change():
	L = str(random.randrange(1, 9))
	file1 = open("data.txt","a")
	file1.writelines(L)

# git commit -m "data updated" --date "2 days ago"
def commit(date):
	os.system("git add .")
	commit = 'git commit -m "data updated " --date "' + str(date) + ' days ago"'
	os.system(commit)
	os.system('git push origin master')

def main():
	for date in range(d_to, d_from+1):
		rand = random.randrange(1, 7)
		if rand==1 or rand==3:
			commit_number = random.randrange(commits_range[0], commits_range[1]+1)
			print("================", date, commit_number)
			for number in range(0, commit_number+1):
				file_change()
				commit(date)
		

if __name__ == '__main__':
	main()