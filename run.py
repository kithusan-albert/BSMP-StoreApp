# Import the create_app function from the bsmp_storeapp 
from bsmp_storeapp import create_app

# Create an instance of the Flask application using the create_app function
app = create_app()

if __name__ == '__main__':
    # Run the application with debugging enabled
    app.run(debug=True)

