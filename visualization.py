import matplotlib.pyplot as plt

def create_optimized_pie_chart(data):
    plt.figure(figsize=(6, 6))
    plt.pie(data['Percentage'], labels=data['Category'], autopct='%1.1f%%')
    plt.title('Optimized Pie Chart')
    plt.show()

optimized_data = {'Category': ['Apple Pie', 'Blueberry Pie'], 'Percentage': [50, 50]}
create_optimized_pie_chart(optimized_data)
