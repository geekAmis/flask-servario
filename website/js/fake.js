function getIP() {
        fetch('/ip')
          .then((res) => res.text())
          .then((data) => document.querySelector('.ipaddress').value=`${data}`);
      }