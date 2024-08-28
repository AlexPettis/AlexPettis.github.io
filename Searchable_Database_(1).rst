.. code:: ipython3

    import pandas as pd
    
    df = pd.read_csv('GroceryDataset.csv')
    df.head()
    
    df_2 = df[['Title', 'Price', 'Feature']]
    
    df_2.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Title</th>
          <th>Price</th>
          <th>Feature</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>David’s Cookies Mile High Peanut Butter Cake, ...</td>
          <td>$56.99</td>
          <td>"10"" Peanut Butter Cake\nCertified Kosher OU-...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>The Cake Bake Shop 8" Round Carrot Cake (16-22...</td>
          <td>$159.99</td>
          <td>Spiced Carrot Cake with Cream Cheese Frosting ...</td>
        </tr>
        <tr>
          <th>2</th>
          <td>St Michel Madeleine, Classic French Sponge Cak...</td>
          <td>$44.99</td>
          <td>100 count\nIndividually wrapped\nMade in and I...</td>
        </tr>
        <tr>
          <th>3</th>
          <td>David's Cookies Butter Pecan Meltaways 32 oz, ...</td>
          <td>$39.99</td>
          <td>Butter Pecan Meltaways\n32 oz 2-Pack\nNo Prese...</td>
        </tr>
        <tr>
          <th>4</th>
          <td>David’s Cookies Premier Chocolate Cake, 7.2 lb...</td>
          <td>$59.99</td>
          <td>"10" Four Layer Chocolate Cake\nCertified Kosh...</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    import pandas as pd
    import ipywidgets as widgets
    from IPython.display import display, HTML, Javascript
    
    # Rename columns
    df_2 = df_2.rename(columns={'Title': 'Item', 'Feature': 'Description'})
    
    # Replace newlines with spaces in the 'Description' column
    df_2['Description'] = df_2['Description'].str.replace('\n', ', ', regex=False)
    
    # Remove "through" and replace with a hyphen in the 'Price' column
    df_2['Price'] = df_2['Price'].str.replace(r'\s*through\s*', '-', regex=True)
    
    # Replace double hyphen with a single hyphen in the 'Price' column
    df_2['Price'] = df_2['Price'].str.replace('--', '-', regex=False)
    
    # Create a separate column for numeric price range (without $ and commas)
    df_2['Price_Numeric'] = df_2['Price'].str.replace(r'[$,]', '', regex=True).str.strip()
    
    # Convert 'Price_Numeric' to a string for processing
    df_2['Price_Numeric'] = df_2['Price_Numeric'].astype(str)
    
    # Convert 'Price_Numeric' column to tuples of floats for easier comparison
    def parse_price_range(price_str):
        price_parts = price_str.split('-')
        if len(price_parts) == 1:
            # Single price, treat as a range with the same start and end
            return (float(price_parts[0].strip()), float(price_parts[0].strip()))
        elif len(price_parts) == 2:
            # Proper range, return as tuple
            return (float(price_parts[0].strip()), float(price_parts[1].strip()))
        else:
            # Unexpected format, handle as needed
            return (None, None)
    
    df_2['Price_Range'] = df_2['Price_Numeric'].apply(parse_price_range)
    
    # Calculate max price from the Price_Range column
    max_price = df_2['Price_Range'].apply(lambda x: x[1] if x[1] is not None else 0).max()
    
    # Create a text box for search
    search_term = widgets.Text(description="Search:")
    
    # Create a button for clearing the search box with "×" as the label
    clear_button = widgets.Button(description='×', layout=widgets.Layout(width='30px'))
    
    # Create a button for search
    search_button = widgets.Button(description="Search")
    
    # Create a range slider for price filter using the numeric price column
    price_slider = widgets.FloatRangeSlider(
        value=[0, max_price],  # Default to start at 0 for minimum price and max_price for maximum price
        min=0,  # Set minimum to 0
        max=max_price,  # Set maximum to the calculated max_price
        step=1,
        description='Price Range:',
        continuous_update=False,
        readout_format='.2f',  # Display two decimals without currency formatting
        style={'description_width': 'initial'},  # Adjust description width
        layout=widgets.Layout(width='600px', margin='10px 0')  # Increase slider width and add margin
    )
    
    # Create a multiple select dropdown for attribute filtering
    attributes = ['Gluten Free', 'Kosher', 'Vegan', 'Non-Dairy', 'Organic', 'Non-GMO']  # Add more attributes as needed
    attribute_dropdown = widgets.SelectMultiple(
        options=attributes,
        description='Attributes:',
        style={'description_width': 'initial'},
        layout=widgets.Layout(width='200px', margin='10px 20px')  # Add margin to the right for spacing
    )
    
    # Create output widget to display results
    output = widgets.Output()
    
    # Function to clear the search box
    def clear_search_box(b):
        search_term.value = ''
    
    # Attach clear function to clear button
    clear_button.on_click(clear_search_box)
    
    # Function to handle search and filter
    def handle_submit(sender=None):
        search_term_value = search_term.value.lower().strip()
        min_price, max_price = price_slider.value
        selected_attributes = attribute_dropdown.value
    
        with output:
            output.clear_output()
    
            # Filter by price range using the numeric price column
            filtered_df = df_2[df_2['Price_Range'].apply(lambda x: min_price <= x[0] and max_price >= x[1])]
    
            # Filter by selected attributes if any are selected
            if selected_attributes:
                # Combine all selected attributes into one regex pattern
                pattern = '|'.join(selected_attributes)
                filtered_df = filtered_df[filtered_df['Description'].str.contains(pattern, case=False, na=False)]
    
            # If search box is empty, display the entire filtered database
            if not search_term_value:
                display(HTML(filtered_df[['Item', 'Description', 'Price']].to_html(index=False)))
            else:
                # Perform search within the filtered data
                search_results = filtered_df[filtered_df['Item'].str.contains(search_term_value, case=False, na=False)]
    
                if search_results.empty:
                    print("No results found.")
                else:
                    display(HTML(search_results[['Item', 'Description', 'Price']].to_html(index=False)))
    
            # Scroll to the top of the output after displaying results
            display(Javascript('window.scrollTo(0, 0);'))
    
    # Attach function to search button
    search_button.on_click(handle_submit)
    
    # Attach function to search box
    search_term.on_submit(handle_submit)
    
    # Attach function to price slider
    price_slider.observe(handle_submit, names='value')
    
    # Attach function to dropdown
    attribute_dropdown.observe(handle_submit, names='value')
    
    # Combine the search button and clear button into one horizontal widget
    buttons_hbox = widgets.HBox([clear_button, search_button])
    
    # Combine the search box with the buttons horizontal box
    search_box_with_buttons = widgets.HBox([search_term, buttons_hbox])
    
    # Arrange the slider and dropdown horizontally with spacing
    filters_hbox = widgets.HBox([price_slider, attribute_dropdown], layout=widgets.Layout(overflow='auto'))
    
    # Arrange the search box with buttons and filters vertically
    search_box_and_filters = widgets.VBox([search_box_with_buttons, filters_hbox])
    search_box_and_output = widgets.VBox([search_box_and_filters, output])
    
    # Display the search box, button, slider, dropdown, and output area at the top
    display(search_box_and_output)
    
    # Initially display the entire database without index
    with output:
        display(HTML(df_2[['Item', 'Description', 'Price']].to_html(index=False)))
    
        # Scroll to the top of the output initially
        display(Javascript('window.scrollTo(0, 0);'))
    



.. parsed-literal::

    VBox(children=(VBox(children=(HBox(children=(Text(value='', description='Search:'), HBox(children=(Button(desc…


