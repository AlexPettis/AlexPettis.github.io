library(shiny)
library(dplyr)
library(DT)

# Load the dataset
df <- read.csv('GroceryDataset.csv')

# Select and rename relevant columns
df <- df %>%
  select(Item = Title, Price, Description = Feature) %>%
  mutate(
    Description = gsub("\n", ", ", Description),  # Replace newlines with commas
    Price = gsub("\\s*through\\s*", "-", Price),  # Replace "through" with hyphen
    Price = gsub("--", "-", Price),               # Replace double hyphen with single
    Price_Numeric = gsub("[$,]", "", Price)       # Remove $ and commas for numeric conversion
  )

# Parse the Price_Numeric column into a numeric range for filtering
df <- df %>%
  mutate(
    Price_Range = strsplit(Price_Numeric, "-") %>% 
      lapply(function(x) if (length(x) == 1) rep(as.numeric(x), 2) else as.numeric(x)) %>% 
      do.call(rbind, .)
  )

# Find the maximum price for the slider range
max_price <- max(df$Price_Range[, 2], na.rm = TRUE)

ui <- fluidPage(
  titlePanel("Grocery Search Tool"),
  
  # Search box with clear button
  fluidRow(
    column(8, textInput("search_term", "Search:", "")),
    column(2, actionButton("clear_button", "×", class = "btn btn-default")),
    column(2, actionButton("search_button", "Search", class = "btn btn-primary"))
  ),
  
  # Price range slider and attribute dropdown
  fluidRow(
    column(6, sliderInput("price_range", "Price Range:", min = 0, max = max_price, 
                          value = c(0, max_price), step = 1, pre = "$")),
    column(6, selectizeInput("attributes", "Attributes:", choices = c("Gluten Free", "Kosher", 
                                                                      "Vegan", "Non-Dairy", 
                                                                      "Organic", "Non-GMO"),
                             multiple = TRUE))
  ),
  
  # DataTable to display the search results
  DTOutput("results_table")
)

server <- function(input, output, session) {
  
  # Reactive expression to handle filtering
  filtered_data <- reactive({
    df_filtered <- df
    
    # Filter by price range
    df_filtered <- df_filtered %>%
      filter(Price_Range[, 1] >= input$price_range[1], 
             Price_Range[, 2] <= input$price_range[2])
    
    # Filter by selected attributes
    if (length(input$attributes) > 0) {
      pattern <- paste(input$attributes, collapse = "|")
      df_filtered <- df_filtered %>%
        filter(grepl(pattern, Description, ignore.case = TRUE))
    }
    
    # Filter by search term
    if (nchar(input$search_term) > 0) {
      df_filtered <- df_filtered %>%
        filter(grepl(input$search_term, Item, ignore.case = TRUE))
    }
    
    df_filtered
  })
  
  # Render the results table
  output$results_table <- renderDT({
    datatable(filtered_data(), options = list(pageLength = 10), rownames = FALSE)
  })
  
  # Clear search box when clear button is pressed
  observeEvent(input$clear_button, {
    updateTextInput(session, "search_term", value = "")
  })
  
  # Trigger search button functionality
  observeEvent(input$search_button, {
    output$results_table <- renderDT({
      datatable(filtered_data(), options = list(pageLength = 10), rownames = FALSE)
    })
  })
}

# Run the application 
shinyApp(ui = ui, server = server)
