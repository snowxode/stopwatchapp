import tkinter as tk
import time
import pdfkit
import os

class Stopwatch(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg='black')
        self.master = master
        self.master.title('Stopwatch')
        self.master.attributes('-fullscreen', True)
        self.master.bind("<Button-1>", self.start_stopwatch)
        self.master.bind("<ButtonRelease-1>", self.stop_stopwatch)
        self.master.bind("<Control-z>", self.quit_app)
        self.master.bind("<Control-x>", self.export_results)
        self.grid(sticky='news')
        self.create_widgets()
        self.click_count = 0
        self.times = []

    def create_widgets(self):
        # Create the stopwatch display
        self.display = tk.Label(self, font=('Arial', 72), bg='black', fg='white')
        #self.display['text'] = '0'
        self.display.pack(expand=True)

        # Center the stopwatch display in the window
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
         # Create the counter label
        self.counter_label = tk.Label(self, font=('Arial', 48), bg='black', fg='#808080')
        self.counter_label['text'] = '0'
        self.counter_label.pack(side='left', padx=(50, 0), pady=(0, 50))
        
        # Create the quit text display
        self.quit_text = tk.Label(self, font=('Arial', 18), bg='black', fg='gray')
        self.quit_text['text'] = 'Ctrl-Z to Quit'
        self.quit_text.pack(side='right', padx=10, pady=10)
        
        # Create the quit text display
        self.quit_text = tk.Label(self, font=('Arial', 18), bg='black', fg='gray')
        self.quit_text['text'] = 'Ctrl-X to Export Results'
        self.quit_text.pack(padx=10, pady=10)

    def start_stopwatch(self, event):
        self.start_time = time.time()
        self.update_time()
        self.click_count += 1
        self.counter_label['text'] = str(self.click_count)
        
    def stop_stopwatch(self, event):
        elapsed_time = time.time() - self.start_time
        self.times.append(elapsed_time)
        #self.display['text'] = '{:.5f}'.format(elapsed_time)
        self.after_cancel(self.timer)

    def update_time(self):
        elapsed_time = time.time() - self.start_time
        #self.display['text'] = '{:.5f}'.format(elapsed_time)
        self.timer = self.after(10, self.update_time)

    def quit_app(self, event):
        self.master.destroy()
        
    def export_results(self, event):
    # Generate the HTML for the PDF
        html = '<h1>Results</h1>'
        for i, time in enumerate(self.times):
            html += '<p>{}: {:.5f}</p>'.format(i+1, time)
        
        # Construct the path to the output PDF file
        output_path = os.path.join(os.getcwd(), 'results.pdf')
        
        # Export the PDF
        pdfkit.from_string(html, output_path)


root = tk.Tk()
app = Stopwatch(master=root)
app.mainloop()
