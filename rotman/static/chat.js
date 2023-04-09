$(function(){
    const lang = $("html").attr("lang");
    let SUCCESS, ERROR;
    if (lang === 'he') {
        SUCCESS = 'כל הכבוד! הצלחת לשכנע את רובורוטמן לבטל את הרפורמה!'
        ERROR = "לא הצלחתי לקבל תשובה, נסו שוב"
    } else {
        SUCCESS = 'Well done! You successfuly convinvced RoboRotman to cancel the reform!'
        ERROR = "Unable to get response, please try again."
    }
    let conversation = [];
    let processing = false;
    const $chatBox = $(".chat-box");
    const $chatInput = $(".chat-input");
    $chatInput.focus();
    const getMessageDiv = function(dir, userInput, html) {
        const messageDiv = $(`<div class="message ${dir}">`)
        const p = $('<p>')
        if (userInput) {
            p.text(userInput)
        } else {
            p.html(html)
        }
        messageDiv.append(p)
        return messageDiv
    }
    $("form.input-container").on("submit", function(event) {
        event.preventDefault();
        if (processing) return;
        const userInput = $chatInput.val();
        if (!userInput) return;
        $chatInput.attr("disabled", true);
        processing = true;
        conversation.push(userInput);
        $chatBox.append(getMessageDiv("right", userInput))
        $chatBox.append(getMessageDiv("left", null,
            '<img src="/static/57-server-outline.gif" alt="loading" width="50" height="50">'))
        $chatBox.scrollTop($chatBox[0].scrollHeight);
        const $lastMessage = $chatBox.find(".message:last-child");
        $.ajax({
            type: "POST",
            url: "/get_response",
            data: {"conversation": JSON.stringify(conversation)},
            success: function(data) {
                let response = data.ai_response;
                let success = false;
                if (response.includes('~~SUCCESS~~')) {
                    response = response.replace('~~SUCCESS~~', '');
                    success = true;
                }
                $lastMessage.find('p').text(response);
                if (success) {
                    $lastMessage.find('p').append('<h4>' + SUCCESS + '</h4>');
                    $chatInput.val("");
                } else {
                    $chatInput.attr("disabled", false);
                    $chatInput.val("");
                    $chatInput.focus();
                    processing = false;
                }
                $chatBox.scrollTop($chatBox[0].scrollHeight);
            },
            error: function() {
                alert(ERROR);
                $chatInput.attr("disabled", false);
                $chatInput.focus();
                processing = false;
            }
        });
    });
})