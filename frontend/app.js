function loadGateways(page, pagesize){
    let query=`{
  paginatedGateways(page:${page}, pageSize:${pagesize}){
    gateways {
      id
      name
      ipAddress
      portNumber
      description
      status
      location
    }
    totalCount
    page
    pageSize
    hasNext
    hasPrevious
  }
 }`
fetch('http://127.0.0.1:8000/gateway/graphql/',{
    method: 'post',
    headers: 
        {'content-type': 'application/json'},
    body: JSON.stringify({query: query})

})

.then(function(response) {
    return response.json();
})
.then(function(data) {
    if (!data.data.paginatedGateways) {
        throw new Error('no data returned');
    }
    else{

        let gateways = data.data.paginatedGateways.gateways;
        let tableBody= document.getElementById('table_body');
        tableBody.innerHTML='';
        gateways.forEach(gt => {
            let row = document.createElement('tr');
            let nameCell = document.createElement('td');
            let link = document.createElement('a');
            link.href =`detail.html?id=${gt.id}`;////
            link.textContent = gt.name;
            nameCell.appendChild(link);
            row.appendChild(nameCell);
            let ipCell = document.createElement('td');
            ipCell.textContent = gt.ipAddress;
            
            row.appendChild(ipCell);
            // tableBody.appendChild(row);
            let portCell = document.createElement('td');
            portCell.textContent = gt.portNumber;
            row.appendChild(portCell);
            tableBody.appendChild(row);

            
        });
        paginationDiv=document.getElementsByClassName('pagination')[0];
        paginationDiv.innerHTML = "";
        let prevSymbol = document.createElement('a');
        if(data.data.paginatedGateways.hasPrevious){

            prevSymbol.href=`javascript:loadGateways(${data.data.paginatedGateways.page-1},${data.data.paginatedGateways.pageSize})`;;
        }
        else{
            prevSymbol.href="#"
        }
            prevSymbol.innerHTML="&laquo";
            paginationDiv.appendChild(prevSymbol);
       
        if(data.data.paginatedGateways.hasPrevious){
            pageNavigate=document.createElement('a');
            pageNavigate.href=`javascript:loadGateways(${data.data.paginatedGateways.page-1},${data.data.paginatedGateways.pageSize})`;
            pageNavigate.innerHTML=data.data.paginatedGateways.page-1;
            pageNavigate.style.display='inline-block';
            paginationDiv.appendChild(pageNavigate);


        }
        let currentPage=document.createElement('a');


        currentPage.href="#";
        currentPage.innerHTML=data.data.paginatedGateways.page;
        currentPage.classList.add("active");
        paginationDiv.appendChild(currentPage);
        


        if(data.data.paginatedGateways.hasNext){
            let nextPage=document.createElement('a');
            nextPage.href=`javascript:loadGateways(${data.data.paginatedGateways.page+1},${data.data.paginatedGateways.pageSize})`;
            nextPage.innerHTML=data.data.paginatedGateways.page+1;
            paginationDiv.appendChild(nextPage);
        }
        
        if (!paginationDiv.querySelector('a:last-child') || paginationDiv.querySelector('a:last-child').innerHTML !== "&raquo") { //// check if the last child is not already the next symbol
            let nextSymbol = document.createElement('a');
            if(data.data.paginatedGateways.hasNext){
                nextSymbol.href=`javascript:loadGateways(${data.data.paginatedGateways.page+1},${data.data.paginatedGateways.pageSize})`;
            }
            else{
                nextSymbol.href="#";

            }
            
            nextSymbol.innerHTML="&raquo";
            paginationDiv.appendChild(nextSymbol);
        }
    }
})
.catch(function(error) {
    console.error("Error loading gateways:", error);
});
}

function loadGatewayDetail(id){
    let query=`{
  gateway(id:${id}){
    id
    name
    ipAddress
    portNumber
    description
    
  }
}`
fetch('http://127.0.0.1:8000/gateway/graphql/',{
    method: 'post',
    headers: 
        {'content-type': 'application/json'},
    body: JSON.stringify({query: query})

})
.then(function(response){
    return response.json();
})
.then(function(data){
    if (!data.data.gateway) {
        throw new Error("Gateway not found");
    }
     let idTag=document.getElementById('id');
     idTag.innerHTML=data.data.gateway.id;

     let nameTag=document.getElementById('name');
     nameTag.innerHTML=data.data.gateway.name;

     let ipTag=document.getElementById('ip');
     ipTag.innerHTML=data.data.gateway.ipAddress;

     let portTag=document.getElementById('port');
     portTag.innerHTML=data.data.gateway.portNumber;

     let descTag=document.getElementById('description');
     descTag.innerHTML=data.data.gateway.description;


   
})

.catch(function(error){
    console.error("Error loading gateway details:", error);
});
}
// loadGateways(1,6);
// const params = new URLSearchParams(window.location.search);////
// const id = params.get("id");

// if (id) {
//   loadGatewayDetail(id);
// }
if (window.location.pathname.endsWith("index.html") || window.location.pathname === "/") {
    loadGateways(1, 5); 
}


if (window.location.pathname.endsWith("detail.html")) {
    const params = new URLSearchParams(window.location.search);
    const id = params.get("id");
    if (id) {
        loadGatewayDetail(id);
    }
}
fetch("sidebar.html")
.then(response => response.text())
.then(html => {
    document.getElementsByClassName('sidebarLoader')[0].innerHTML= html;
})
