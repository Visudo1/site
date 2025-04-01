<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Final</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
		<srcript ="https://cdn.tailwind.com"></srcript>
</head>
<body class="bg-cover bg-center" style="background-image: url('.jpg');">

    <!-- Navbar -->
    <nav class="bg-gray-800 bg-opacity-75 w-full p-4 fixed top-0 z-50">
        <div class="container mx-auto flex justify-between items-center">
            <a href="#" class="text-white text-lg font-bold">Brand</a>
            <ul class="flex space-x-4">
                <li><a href="#" class="text-white hover:bg-gray-700 px-3 py-2 rounded">Home</a></li>
                <li><a href="#" class="text-white hover:bg-gray-700 px-3 py-2 rounded">About</a></li>
                <li><a href="#" class="text-white hover:bg-gray-700 px-3 py-2 rounded">Services</a></li>
                <li><a href="#" class="text-white hover:bg-gray-700 px-3 py-2 rounded">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="flex items-center justify-center h-screen pt-16"> <!-- Add pt-16 to push content below the navbar -->
        <div class="text-center">
            <h1 class="text-white text-4xl md:text-6xl font-bold mb-4">Welcome to Our Page</h1>
            <p class="text-white text-lg md:text-2xl">This is a demo page using Tailwind CSS with a full-screen background.</p>
        </div>
    </main>
    
    <main>
        <button onclick="getUserInput()">Click me</button>

    <script>
        function getUserInput() {
            let name = prompt("Please enter your name", "Edo Erpani");
            if (name !== null) {
                alert("Hello, " + name + "!");
            } else {
                alert("No name entered.");
            }
        }
    </script>
       
    </main>
    
</body>
<foot>
		<footer>
				<p>Copyright &copy; 2022-2025 Eunoia Industry Techologies</p>
		</footer>
</foot>
</html>
