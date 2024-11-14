function copy_to_clipboard() {
    document.getElementById("copybtn").innerText = "Copied!";
    var copyText = document.getElementById("key");
    navigator.clipboard.writeText(copyText.innerText);
  }