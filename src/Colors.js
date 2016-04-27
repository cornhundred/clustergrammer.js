// colors from http://graphicdesign.stackexchange.com/revisions/3815/8
var all_colors;

all_colors = [ "#393b79", "#bcbd22", "#aec7e8", "#ff7f0e", "#ffbb78", "#98df8a", 
    "#404040", "#ff9896", "#9467bd", "#c5b0d5", "#e7969c", "#8c564b", "#1f77b4", 
    "#5254a3", "#c49c94", "#e377c2", "#7f7f7f", "#2ca02c", 
    "#dbdb8d", "#17becf", "#637939", "#6b6ecf", "#9c9ede", "#d62728", 
    "#8ca252", "#8c6d31", "#bd9e39", "#e7cb94", "#843c39", "#ad494a", "#d6616b", 
    "#7b4173", "#a55194", "#ce6dbd", "#de9ed6"]; 

  // too light colors 
  // "#c7c7c7", 
  // "#f7b6d2", 
  // "#cedb9c", 
  // "#9edae5", 

function get_default_color() {
  return '#EEE';
}

function get_random_color(i) {
  return all_colors[i % get_num_colors()];
}

function get_num_colors() {
  return all_colors.length;
}

module.exports = {
  get_default_color: get_default_color,
  get_random_color: get_random_color,
  get_num_colors: get_num_colors
};
