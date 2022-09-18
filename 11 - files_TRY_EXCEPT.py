#
# 
# 
# 
# 
# 
#  fin = open('oldfile.txt','r')    
#
# firstLine = fin.readline()
# print(firstLine)
# secondLine = fin.readline()
# print(secondLine)
# thirdLine = fin.readline()
# print(thirdLine)
#
# fin.close()



# fin = open('LWP.txt', 'r')
#
# print(fin.readlines())         READ ALL LINES
#
# fin.close()




# fin = open('LWP.txt', 'r')
#
# for line in fin:
#     print(line)
#
# fin.close()




# fin = open('LWP.txt','r')
#
# print(fin.read()) READ WHOLE FILE ATONCE,      READ(10) FIRST 10 CHARACTERS OF FILE
#
# fin.close()






# fin = open('LWP.txt', 'a')     APPEND MODE APPEND TO FILE
#
# #fin.write("\nThis is a new Line that we've just written\n")
# newLines = ['this is line1\n',
#             'this is line2\n',
#             'this is line3\n']
# fin.writelines(newLines)
#
# fin.close()







# fin = open('newFile.txt', 'w')        WRITE MODE OVERRIDE A FILE
#
# # newLines = ['this is line1\n',
# #             'this is line2\n',
# #             'this is line3\n']
# # fin.writelines(newLines)
#
# newLines = ['this overwrites the first line \n',
#             'this overwrites the second line \n',
#             'this overwrites the third line \n']
# fin.writelines(newLines)
#
# fin.close()




try:
    with open('LWP.txt', 'r') as fin:       # CHECKS FOR READ PERMISSIONS AND CLOSES AUTOMATICALLY
        firstLine = fin.readline()
        print(firstLine)
        secondLine = fin.readline()
        print(secondLine)
        thirdLine = fin.readline()
        print(thirdLine)

    # fin = open('oldfile.txt', 'r')
    #
    # firstLine = fin.readline()
    # print(firstLine)
    # secondLine = fin.readline()
    # print(secondLine)
    # thirdLine = fin.readline()
    # print(thirdLine)
    #
    # fin.close()

except:
    print("Error: We cannot find or open the file , please check your code")

print(5+6)
