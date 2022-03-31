def delivery_report(daily_file): #defines a function that takes in file daily_file

    the_file = open(daily_file) #opens file and names it the_file
    
    for line in the_file: #for loop goes through each line
        line = line.rstrip() #clears extra chars on each line
        words = line.split('|') #splits string into list separated by |

        melon = words[0] #defines melon as first list item (melon type)
        count = words[1] #defines count as second list item (number sold)
        amount = words[2] #defines amount as third list item (total price)

        print(f"Delivered {count} {melon}s for total of ${amount}") #prints statement
    the_file.close() #closes file

print("Day 1") #prints Day 1
delivery_report('um-deliveries-day-1.txt') #calls report for this file

print("Day 2") #prints Day 2
delivery_report("um-deliveries-day-2.txt") #calls report for this file

print("Day 3") #prints day 3
delivery_report("um-deliveries-day-3.txt") #calls report for this file