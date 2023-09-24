var display = true

function clickMenu()
{
    if (display == true)
    {
        itens.style.transform = "translateX(0)"
        display = false
    } else
    {
        itens.style.transform = "translateX(-100%)"
        display = true
    }

}