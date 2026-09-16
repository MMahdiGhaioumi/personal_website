document.addEventListener("DOMContentLoaded", function () {

    const parentInput =
        document.getElementById("comment-parent");

    const replyInfo =
        document.getElementById("reply-info");

    const replyUser =
        document.getElementById("reply-user");

    const cancelReply =
        document.getElementById("cancel-reply");

    const commentForm =
        document.getElementById("comment-form");


    // Reply
    document.addEventListener("click", function (event) {

        const button =
            event.target.closest(".reply-button");

        if (!button) {
            return;
        }

        const commentId =
            button.dataset.commentId;

        const commentName =
            button.dataset.commentName;


        // قرار دادن parent
        parentInput.value = commentId;


        // نمایش نام شخص
        replyUser.textContent = commentName;

        replyInfo.hidden = false;


        // رفتن به فرم
        commentForm.scrollIntoView({
            behavior: "smooth",
            block: "center"
        });

    });


    // لغو Reply
    cancelReply.addEventListener(
        "click",
        function () {

            parentInput.value = "";

            replyUser.textContent = "";

            replyInfo.hidden = true;

        }
    );

});