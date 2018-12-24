# Make dummy variables for rank
one_hot_data = pd.concat([data, pd.get_dummies(data['rank'], prefix='rank')], axis=1)

# Drop the previous rank column
one_hot_data = one_hot_data.drop('rank', axis=1)

# Print the first 10 rows of our data
one_hot_data[:10]

# Copying our data
processed_data = one_hot_data[:]

# Scaling the columns
processed_data['gre'] = processed_data['gre']/800
processed_data['gpa'] = processed_data['gpa']/4.0
processed_data[:10]



def error_term_formula(x, y, output):
    return (y - output)*sigmoid_prime(x)


## alternative solution ##
# you could also *only* use y and the output
# and calculate sigmoid_prime directly from the activated output!

# below is an equally valid solution (it doesn't utilize x)
def error_term_formula(x, y, output):
    return (y-output) * output * (1 - output)