# python-challenge

update 9/28/2023

I've added new python files that should show code using basic python functions rather than pandas. Apologies, I'm finding it difficult with the timing of the homework and classes to work purely in python for homework while activiely learning pandas. I will work on this going forward. 



I used online resources for some areas I got stuck with (listed blow)

For python bank I used online resources for the following parts of my code:
format='%b-%y'
I found this online to convert abbrevations to date time object

total_months = len(data['Date'].dt.to_period('M').unique()) 
I used an online resources for the 'M' part of this code to convert the the date data into monthly frequency

${:,.2f}
Since I was already looking into code to help with formatting the abbreviations, I decided to look into how I could format the data to output commas and $ rather than a jumble of numbers and found this code

${max_increase:,.2f} 
for increase and decrease I used similar formatting that I found online. I find it helpful to change the formatting to reflect the output rather than have just a bunch of numbers
