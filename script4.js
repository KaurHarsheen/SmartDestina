var NorthDelhi= ["India Gate", "Humayun's Tomb","Akshardham Temple","Waste to Wonder Park","Jantar Mantar","Chandni Chowk","Lotus Temple",
"Red Fort","Agrasen ki Baoli","Sunder Nursery","Garden of Five Senses","Lodhi Garden","National Gallery of Modern Art",
"National Zoological Park","Qutub Minar","National Science Centre"]

var Mumbai= ["Marine Drive","Gateway of India","Chhatrapati Shivaji Maharaj Vastu Sangrahalaya","Sanjay Gandhi National Park",
    "Siddhivinayak Temple","Mahalaxmi Temple","Haji Ali Dargah","Chowpatty Beach","Essel World","Elephanta Caves"]

var Lonavala =["Imagicaa"]

var Bangalore=["Bangalore Palace","Lalbagh Botanical Garden","Cubbon Park","Vidhana Soudha","ISKCON Temple Bangalore"]

var Hyderabad=["Charminar","Golconda Fort","Hussain Sagar Lake","Ramoji Film City","Salar Jung Museum","Qutb Shahi Tombs",
    "Birla Mandir","Chowmahalla Palace","Nehru Zoological Park","Lumbini Park"]

var Kolkata=["Victoria Memorial","Howrah Bridge","Indian Museum","Dakshineswar Kali Temple","Kalighat Kali Temple",
    "Eden Gardens","Alipore Zoological Gardens","Science City Kolkata","Belur Math","Marble Palace"]

var NorthGoa=["Calangute Beach","Fort Aguada","Anjuna Beach","Chapora Fort","Se Cathedral",
    "Baga Beach","Arambol Beach","Palolem Beach","Miramar Beach","Aguada Beach",]

var SouthGoa=["Basilica of Bom Jesus","Dudhsagar Falls","Colva Beach","Dr. Salim Ali Bird Santuary"]

    $("#inputDistrict").change(function(){
        var DistrictSelected = $(this).val();
        var optionsLists;
        var htmlStrings= "";
      
        switch (DistrictSelected) {
          case "NorthDelhi":
              optionsLists = NorthDelhi;
              break;
          case "Mumbai":
              optionsLists = Mumbai;
              break;
          case "Lonavala":
              optionsLists = Lonavala;
              break;
          case "Bangalore":
              optionsLists = Bangalore;
              break;
          case "Hyderabad":
                optionsLists = Hyderabad;
              break;
          case "Kolkata":
                optionsLists = Kolkata;
                break;
          case "NorthGoa":
                optionsLists = NorthGoa;
                break;
          case "SouthGoa":
                optionsLists = SouthGoa;
                break;         
        }

        for(var i = 0; i < optionsLists.length; i++){
            htmlStrings = htmlStrings+"<option value='"+ optionsLists[i] +"'>"+ optionsLists[i] +"</option>";
          }
          $("#inputPlace").html(htmlStrings);
    });