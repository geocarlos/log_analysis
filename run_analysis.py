from log_analysis import *

print("\n1. The most popular three articles of all time: \n")
for a in get_top_articles():
    print(a[0] + " - " + str(a[1]) + " views")

print("\n\n2. The most popular article authors of all time: \n")
for a in get_top_authors():
    print(a[0] + " - " + str(a[1]) + " views")

print('\n\n3. Days when more than 1% of requests led to errors: \n')
for a in get_error_days():
    print(a[0] + " - " + format(a[1], '.2g') + "% errors")
print("\n")
