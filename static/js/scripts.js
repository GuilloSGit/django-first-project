document.addEventListener("DOMContentLoaded", function () {
    setTimeout(() => {
        const buttons = document.querySelectorAll('.mark-done-btn');
        buttons.forEach(button => {
            button.addEventListener('click', function () {
                const taskId = this.getAttribute('data-task-id');
                fetch(`/mark-as-done/${taskId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': '{{ csrf_token }}',
                        'Content-Type': 'application/json'
                    },
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.status === 'success') {
                            location.reload();
                        }
                    })
            })
        })

        const deleteButtons = document.querySelectorAll('.delete-task');
        deleteButtons.forEach(buttonX => {
            buttonX.addEventListener('click', function() {
                const taskId = this.getAttribute('data-task-id');
                fetch(`/soft-delete/${taskId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': '{{ csrf_token }}',
                        'Content-Type': 'application/json'
                    },  
                })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        location.reload();
                    }
                })
            })
        })
    }, 1000)

});